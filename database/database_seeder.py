from ..Controller.schedule_parser import ScheduleParser


class DatabaseSeeder:
    def seed(self):
        query = list()
        parser = ScheduleParser()
        parser.parse_schedule()
        schedule = parser.get_schedule()

        for day in schedule:
            for i in range(schedule[day]):
                a = 1


if __name__ == '__main__':
    seeder = DatabaseSeeder()
    seeder.seed()