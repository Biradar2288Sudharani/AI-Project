class TraceService:

    @staticmethod
    def create_trace():

        return []

    @staticmethod
    def add_trace(
        trace,
        reasoning,
        action,
        result
    ):

        trace.append({
            "reasoning": reasoning,
            "action": action,
            "result": result
        })

        return trace