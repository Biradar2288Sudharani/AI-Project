from app.databases.db import SessionLocal

from app.models.patient import Patient
from app.models.summary import Summary
from app.models.conflict import Conflict
from app.models.trace import Trace


class DatabaseService:

    @staticmethod
    def save_patient(data):

        db = SessionLocal()

        try:

            patient = Patient(
                patient_id=data.get(
                    "patient_id",
                    "UNKNOWN"
                ),
                patient_name=data.get(
                    "patient_name"
                ),
                admission_date=data.get(
                    "admission_date"
                ),
                discharge_date=data.get(
                    "discharge_date"
                )
            )

            db.add(patient)
            db.commit()

            return patient.id

        except Exception as e:

            db.rollback()

            print(
                f"Patient Save Error: {e}"
            )

            return None

        finally:

            db.close()

    @staticmethod
    def save_summary(
        patient_id,
        summary_text,
        status="DRAFT"
    ):

        db = SessionLocal()

        try:

            summary = Summary(
                patient_id=patient_id,
                summary_text=summary_text,
                status=status
            )

            db.add(summary)

            db.commit()

            return True

        except Exception as e:

            db.rollback()

            print(
                f"Summary Save Error: {e}"
            )

            return False

        finally:

            db.close()

    @staticmethod
    def save_conflict(
        patient_id,
        conflict_type,
        description
    ):

        db = SessionLocal()

        try:

            conflict = Conflict(
                patient_id=patient_id,
                conflict_type=conflict_type,
                description=description
            )

            db.add(conflict)

            db.commit()

            return True

        except Exception as e:

            db.rollback()

            print(
                f"Conflict Save Error: {e}"
            )

            return False

        finally:

            db.close()

    @staticmethod
    def save_trace(
        patient_id,
        trace_data
    ):

        db = SessionLocal()

        try:

            for item in trace_data:

                trace = Trace(
                    patient_id=patient_id,
                    step_number=trace_data.index(item) + 1,
                    reasoning=item.get(
                        "reasoning"
                    ),
                    action=item.get(
                        "action"
                    ),
                    result=item.get(
                        "result"
                    )
                )

                db.add(trace)

            db.commit()

            return True

        except Exception as e:

            db.rollback()

            print(
                f"Trace Save Error: {e}"
            )

            return False

        finally:

            db.close()