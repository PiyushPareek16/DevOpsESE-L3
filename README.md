# jenkins-webhook-trigger

App: `weather-monitor`

This repo demonstrates triggering a Jenkins build automatically via a GitHub webhook on each commit.

## Contents
- `weather-monitor/` Minimal Flask app with `Dockerfile`
- `Jenkinsfile` Jenkins pipeline with `githubPush()` trigger and Docker build

## Prerequisites
- Jenkins with the following:
  - Git plugin
  - GitHub plugin (for `githubPush()` trigger)
  - Docker installed on the Jenkins agent
- A GitHub repository (this repo once pushed)

## Local build (optional)
```bash
cd weather-monitor
docker build -t weather-monitor:local .
# Run it
docker run --rm -p 8080:8080 weather-monitor:local
# Test
curl -s http://localhost:8080/
```

## Jenkins setup (Pipeline from SCM)
1. Create a GitHub repo and push this code (see commands section below).
2. In Jenkins, create a new job → Pipeline → name: `jenkins-webhook-trigger`.
3. Select “Pipeline script from SCM”.
   - SCM: Git
   - Repository URL: the Git URL of your GitHub repo
   - Credentials: your GitHub credentials/token if needed
   - Script Path: `Jenkinsfile`
4. In “Build Triggers”, check “GitHub hook trigger for GITScm polling”.
5. Save.

## GitHub webhook configuration
1. In your GitHub repo → Settings → Webhooks → Add webhook.
2. Payload URL: `http(s)://<your-jenkins-host>/github-webhook/`
   - Example: `https://jenkins.example.com/github-webhook/`
3. Content type: `application/json`.
4. Secret: set a secret and configure the same secret in Jenkins global GitHub config (Manage Jenkins → Configure System → GitHub → Add GitHub Server → Credentials/Secret).
5. Which events: “Just the push event”.
6. Add webhook.

When you push a commit, GitHub sends a webhook to Jenkins; Jenkins triggers the job due to `githubPush()` and the job builds the Docker image defined in `weather-monitor/Dockerfile`.

## Expected output
- A Jenkins build automatically starts after a push.
- Console log includes “Build succeeded after webhook trigger.” on success.

## Commands: initialize, commit, push
Replace placeholders in angle brackets.
```bash
cd "/Users/pranshugupta/Desktop/untitled folder 4"

git init

git branch -m main

git add .

git commit -m "feat: weather-monitor app with Jenkins webhook pipeline"

git remote add origin git@github.com:<your-org>/<jenkins-webhook-trigger>.git
# or: https://github.com/<your-org>/<jenkins-webhook-trigger>.git

git push -u origin main
```

## Verify webhook delivery
- In GitHub → Repo → Settings → Webhooks → click the webhook → “Recent Deliveries” should show 200 response.
- In Jenkins, the job should trigger almost immediately and run the stages: Checkout, Build, Test, Image Inspect.

## Notes
- For Multibranch Pipelines, configure a GitHub Branch Source and Jenkins will register the webhook; the `githubPush()` trigger is not needed in that case.
- Ensure the Jenkins controller/agent has Docker access. If using an agent node, label it and set `agent { label 'docker' }` in the `Jenkinsfile`.

