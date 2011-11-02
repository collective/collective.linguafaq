from plone.app.contentrules.handlers import execute_rules

def view_called(event):
    execute_rules(event)
