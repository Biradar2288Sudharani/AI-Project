from app.tools.trace_logger import TraceLogger

logger = TraceLogger()

logger.add_step(
    reasoning="Need diagnosis",
    action="Read PDF",
    result="Diagnosis found"
)

print(logger.get_trace())