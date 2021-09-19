class GetLocationIntentHandler(AbstractRequestHandler):
    """Handler for GetLocation Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetLocation")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # geolocation = handler_input.request_envelope.context.system.device.supported_interfaces.geolocation
        # if geolocation is not None:
        try:
            req_envelope = handler_input.request_envelope
            response_builder = handler_input.response_builder

            supported_interfaces = get_supported_interfaces(handler_input)
            logger.info("Supported interfaces: {}".format(supported_interfaces))

            geolocation_supported = getattr(supported_interfaces, 'geolocation', None)

            logger.info("geolocation supported: {}".format(geolocation_supported))
            if geolocation_supported is None:
                response_builder.speak(NOTIFY_DEVICE_UNSUPPORTED).set_should_end_session(True)
                return response_builder.response

            # Check if permissions set
            geolocation_context = req_envelope.context.geolocation
            if geolocation_context is None:
                perms = req_envelope.context.system.user.permissions.scopes
                logger.info("Permissions available: {}".format(perms))
                geo_perm = perms.get("alexa::devices:all:geolocation:read", None)

                # Check if skill has permissions to use location data
                if geo_perm is None or geo_perm.status != PermissionStatus.GRANTED:
                    response_builder.speak(NOTIFY_MISSING_PERMISSIONS).set_card(AskForPermissionsConsentCard(permissions=permissions))
                    return response_builder.response
                else:
                    response_builder.speak(NOTIFY_MISSING_DEVICE_LOC_SHARING).ask(NO_LOCATION_INFO_WITH_PERM)
                    return response_builder.response
            else:
                # Permission available, check if device sharing location
                logger.info("Location info: {}".format(geolocation_context))

                # location_services = geolocation_context.location_services
                # if (location_services is None or location_services.status != Status.RUNNING
                #         or location_services.access != Access.ENABLED):
                #     response_builder.speak(NOTIFY_MISSING_DEVICE_LOC_SHARING).ask(
                #         NO_LOCATION_INFO_WITH_PERM)
                #     return response_builder.response

                # Device location sharing on
                if geolocation_context.coordinate is None:
                    # Location retrieval failure, try again message
                    response_builder.speak(LOCATION_FAILURE).ask(LOCATION_FAILURE)
                    return response_builder.response
                else:
                    # Got location, do further processing if needed
                    # Check freshness and accuracy, etc.
                    accuracy = geolocation_context.coordinate.accuracy_in_meters
                    latitude = geolocation_context.coordinate.latitude_in_degrees
                    longitude = geolocation_context.coordinate.longitude_in_degrees
                    # https://www.google.com/maps/place/22%C2%B038'32.6%22N+88%C2%B013'18.2%22E
                    location_url = "https://www.google.com/maps/place/"+deg_to_dms(latitude)+"+"+deg_to_dms(longitude, 'lon')
                    location = SAMPLE_LOCATION_DATA.format(latitude, longitude, accuracy)
                    response_builder.speak(location).set_should_end_session(True).set_card(SimpleCard("Your location", location+"\nurl: "+location_url))
                    return response_builder.response
                    
        except Exception as e:
            response_builder.speak(str(e))
            return response_builder.response