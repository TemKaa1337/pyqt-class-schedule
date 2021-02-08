from database.database_schema import DatabaseSchema as Schema
from database.database_seeder import DatabaseSeeder as Seeder
from Controller.schedule_parser import ScheduleParser as Parser


class InitializeProject:
    def initialize(self):
        schema = Schema()
        schema.refresh()
        parser = Parser()
        parser.parse_schedule()
        schedule_info = parser.get_schedule()
        seeder = Seeder(schedule_info)
        seeder.seed()


if __name__ == '__main__':
    initialize = InitializeProject()
    initialize.initialize()
