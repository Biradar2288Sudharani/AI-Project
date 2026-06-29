class MedicationReconciliation:

    @staticmethod
    def compare(
        admission_meds: list,
        discharge_meds: list
    ):

        added = []
        removed = []
        unchanged = []

        admission_set = set(
            [med.lower() for med in admission_meds]
        )

        discharge_set = set(
            [med.lower() for med in discharge_meds]
        )

        for med in discharge_set:
            if med not in admission_set:
                added.append(med)

        for med in admission_set:
            if med not in discharge_set:
                removed.append(med)

        for med in admission_set:
            if med in discharge_set:
                unchanged.append(med)

        return {
            "added": added,
            "removed": removed,
            "unchanged": unchanged
        }