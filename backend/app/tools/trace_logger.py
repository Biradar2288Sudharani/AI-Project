class TraceLogger:

    def __init__(self):
        self.steps = []

    def add_step(
        self,
        reasoning,
        action,
        result
    ):

        self.steps.append({
            "reasoning": reasoning,
            "action": action,
            "result": result
        })

    def get_trace(self):
        return self.steps