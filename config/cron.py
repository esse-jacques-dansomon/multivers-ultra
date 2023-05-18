from django_cron import CronJobBase, Schedule


class BackupCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Run the backup job every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'config.cron.backup'  # A unique code for your cron job

    def do(self):
        from django.core.management import call_command
        call_command('dbbackup')  # Execute the dbbackup management command
