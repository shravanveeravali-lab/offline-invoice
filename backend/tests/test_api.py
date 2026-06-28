from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["mode"] == "offline"


def test_upload_rejects_unsupported_file() -> None:
    response = client.post(
        "/upload",
        files={"file": ("invoice.exe", b"bad", "application/octet-stream")},
    )
    assert response.status_code == 400


def test_upload_accepts_text_invoice(tmp_path: Path) -> None:
    response = client.post(
        "/upload",
        files={"file": ("invoice.txt", b"ABC\nTotal: 10", "text/plain")},
    )
    assert response.status_code == 200
    assert response.json()["stored_path"].endswith(".txt")
