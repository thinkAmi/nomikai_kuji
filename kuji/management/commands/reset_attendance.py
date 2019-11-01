from django.core.management import BaseCommand

from kuji.models import Member, Seat


class Command(BaseCommand):
    def handle(self, *args, **options):
        # seatは0クリア
        Member.objects.update(seat=None)

        # Seatは一度ゼロリセット
        Seat.objects.all().delete()

        # Memberのis_attendanceがTrueの件数分、1から番号を作成する
        attendees = Member.objects.filter(is_attendance=True)

        for i in range(1, len(attendees) + 1):
            Seat.objects.create(rest_no=i)
