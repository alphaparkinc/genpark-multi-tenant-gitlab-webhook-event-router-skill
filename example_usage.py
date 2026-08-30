from client import MultiTenantGitlabWebhookEventRouterClient

def main():
    client = MultiTenantGitlabWebhookEventRouterClient()
    res = client.route_gitlab_event('pipeline_event', {'object_attributes': {'status': 'success'}})
    print('GitLab Webhook Router: ' + res['event_dispatch_id'] + ' (' + res['event_type'] + ')')
    print('Subscribers: ' + str(res['subscribers_notified_count']) + ' | Signature Verified: ' + str(res['signature_verification_passed']))
    print('Review Triggered: ' + str(res['automated_pr_review_triggered']) + ' in ' + str(res['dispatch_latency_ms']) + 'ms')
    print('Audit Stream: ' + res['event_audit_stream_url'])

if __name__ == '__main__':
    main()
