# CI/CD Pipeline Project

An end-to-end **CI/CD pipeline** that automatically builds, tests, containerizes,
and deploys a web application on every code change — using **GitHub Actions**,
**Jenkins**, **Docker**, and **AWS EC2**.

This project demonstrates the core DevOps workflow of continuous integration and
continuous delivery: code pushed to GitHub is automatically validated, packaged
into a Docker image, and deployed, with a rollback path if anything fails.

---

## Architecture / Workflow

```
Developer → git push → GitHub
                          │
                          ▼
                  CI/CD Pipeline (GitHub Actions / Jenkins)
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
     Test stage      Build Docker      Deploy to
     (pytest)          image           AWS EC2
        │                 │                 │
        └── fail? ────────┴── stop pipeline ┘
                          │
                     on failure →
                     rollback to
                   last stable image
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| **Git & GitHub** | Source control and pipeline trigger |
| **GitHub Actions** | CI/CD pipeline (`.github/workflows/ci-cd.yml`) |
| **Jenkins** | Alternative CI/CD pipeline (`Jenkinsfile`) |
| **Docker** | Containerizes the app for consistent environments |
| **pytest** | Automated tests run before every build |
| **AWS EC2** | Deployment target (host running the container) |

---

## Pipeline Stages

1. **Checkout** — pulls the latest code from GitHub.
2. **Test** — runs automated tests (`pytest tests/`). If tests fail, the pipeline
   stops here and nothing is deployed.
3. **Build** — builds a Docker image, tagged with the commit SHA / build number
   so every deployment is traceable.
4. **Deploy** — deploys the container (on the `main` branch only).
5. **Rollback** — if deployment fails, the pipeline restarts the last known-good
   container image.

---

## How to Run Locally

```bash
# 1. Build the Docker image
docker build -t ci-cd-pipeline-app .

# 2. Run the container
docker run -d -p 80:80 ci-cd-pipeline-app

# 3. Open http://localhost in a browser

# 4. Run tests
pip install pytest
pytest tests/ -v
```

The GitHub Actions pipeline runs automatically on every push to `main`.
You can see runs under the **Actions** tab of this repository.

---

## Key DevOps Concepts Demonstrated

- **Continuous Integration:** every push is automatically tested and built.
- **Continuous Delivery:** successful builds are automatically deployed.
- **Fail-fast:** the pipeline stops immediately if tests fail, so broken code
  never reaches deployment.
- **Traceability:** each image is tagged with the commit SHA / build number.
- **Rollback:** a failed deploy automatically reverts to the last stable image.
