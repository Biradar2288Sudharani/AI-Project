class MissingDataChecker:

    REQUIRED_FIELDS = [
        "patient_name",
        "admission_date",
        "discharge_date",
        "principal_diagnosis",
        "hospital_course",
        "discharge_condition"
    ]

    @classmethod
    def check(cls, data):

        missing_fields = []

        for field in cls.REQUIRED_FIELDS:

            value = data.get(field)

            if not value:
                missing_fields.append(field)

        pending_items = data.get(
            "pending_results",
            []
        )

        return {
            "missing_fields": missing_fields,
            "pending_items": pending_items,
            "needs_review":
                len(missing_fields) > 0
                or len(pending_items) > 0
        }