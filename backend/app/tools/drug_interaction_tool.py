class DrugInteractionTool:

    @staticmethod
    def check(medications):

        interactions = []

        meds = [m.lower() for m in medications]

        if (
            "warfarin" in meds
            and "aspirin" in meds
        ):
            interactions.append(
                "Potential bleeding risk"
            )

        return interactions