from app.tools.conflict_detector import ConflictDetector

result = ConflictDetector.detect(
    "Diabetes",
    "Hypertension"
)

print(result)