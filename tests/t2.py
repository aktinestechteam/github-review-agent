from github_review_agent.email.email_service import EmailService
from github_review_agent.email.templates import approval_email

service = EmailService()

html = approval_email(
    pr_title="Add Login API",
    summary="Authentication improvements.",
    risk="Medium",
    approve_url="https://localhost:8000/approve",
    reject_url="https://localhost:8000/reject",
)

service.send(
    to_email="lgogave@gmail.com",
    subject="PR Approval Required",
    html=html,
)

print("Email sent")