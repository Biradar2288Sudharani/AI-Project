class EscalationTool:

    @staticmethod
    def escalate(reason):

        return {
            "status": "REVIEW_REQUIRED",
            "reason": reason
        }