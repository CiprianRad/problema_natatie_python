from ro.ubb.duckapp.domain.validators import DuckValidator, LaneValidator
from ro.ubb.duckapp.repository.file_repository import FileRepository
from ro.ubb.duckapp.repository.generic_repository import Repository
from ro.ubb.duckapp.service.duck_service import DuckService
from ro.ubb.duckapp.service.lane_service import LaneService
from ro.ubb.duckapp.service.reports_service import ReportsService
from ro.ubb.duckapp.ui.console import AppConsole

def main():
    duck_validator = DuckValidator()
    lane_validator = LaneValidator()
    # duck_repository = Repository(duck_validator)
    # lane_repository = Repository(lane_validator)
    duck_repository = FileRepository(duck_validator, "../../../../data/natatie.in")
    lane_repository = FileRepository(lane_validator, "../../../../data/natatie.in")
    duck_service = DuckService(duck_repository)
    lane_service = LaneService(lane_repository)
    reports_service = ReportsService(duck_repository, lane_repository)
    app_console = AppConsole(duck_service, lane_service, reports_service)
    app_console.run_menu()
main()