from apscheduler.schedulers.asyncio import AsyncIOScheduler

from github_review_agent.scheduler.jobs.scan_pull_requests import (
    scan_pull_requests,
)

scheduler = AsyncIOScheduler()

scheduler.add_job(
    scan_pull_requests,
    trigger="interval",
    minutes=5,
    id="scan_pull_requests",
    replace_existing=True,
)

def start_scheduler():
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown()