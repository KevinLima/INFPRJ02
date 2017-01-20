# Met deze functie kan je checken of een event TRUE is
# Importeren:   " from EventsHelper import event_exist "
# Gebruiken:    " if event_exist(events, pygame.QUIT): "


def event_exist(event_list, event_type):
    for event in event_list:
        if event.type == event_type:
            return True
    return False
