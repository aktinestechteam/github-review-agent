def approval_email(
    pr_title: str,
    summary: str,
    risk: str,
    approve_url: str,
    reject_url: str,
) -> str:

    return f"""
    <h2>GitHub Pull Request Approval</h2>

    <p><b>PR:</b> {pr_title}</p>

    <p><b>Summary:</b></p>

    <p>{summary}</p>

    <p><b>Risk:</b> {risk}</p>

    <hr>

    <a href="{approve_url}">
        ✅ Approve
    </a>

    <br><br>

    <a href="{reject_url}">
        ❌ Reject
    </a>
    """