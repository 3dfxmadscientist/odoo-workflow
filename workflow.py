class State(Object):
    string = None
    action = None
    def __init__(self, string, action=None):
        self.ref = ref
        self.action = action
        
        


class Transition(Object):
    state_from = None
    state_into = None
    validation = None
    logic = None
    
    def __init__(self, state_from, state_into, logic="or", validation=None):
        self.state_from = state_from
        self.state_into = state_into
        self.logic = logic
        self.validation = validation

    def validate(self):
        pass

class Workflow(Object):
    state = None
    states = []
    transitions = []
    
    
wkf = Workflow()    

def actionNew():
    pass

def validationNewStarted():
    pass    


wkf.addState(State('new',actionNew))
wkf.addState(State('started',actionStarted))
wkf.addState(State('completed',actionCompleted))

wkf.addTransition('new','started',validationNewStarted)
wkf.addTransition('new','completed',validationNewCompleted)

wkf.addTransition('started','completed',validationStartedCompleted)