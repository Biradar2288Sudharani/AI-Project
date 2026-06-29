class ConflictDetector:

    @staticmethod
    def detect(
        admission_diagnosis,
        discharge_diagnosis
    ):

        conflicts = []

        if (
            admission_diagnosis
            and discharge_diagnosis
            and admission_diagnosis.lower()
            != discharge_diagnosis.lower()
        ):
            conflicts.append({
                "type": "diagnosis_conflict",
                "message":
                f"Admission: {admission_diagnosis} | "
                f"Discharge: {discharge_diagnosis}"
            })

        return conflicts