# Met deze functie kan je checken of een event TRUE is
# Importeren:   " from EventsHelper import EventExist "
# Gebruiken:    " if EventExist(events, pygame.QUIT): "

def EventExist(eventList, eventType):
    for event in eventList:
        if event.type == eventType:
            return True
    return False