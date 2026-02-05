import pytest


@pytest.mark.asyncio
async def test_create_user_api(client):
    response = await client.post(
        "/users/",
        json={
            "name": "John",
            "email": "john@mail.com"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["email"] == "john@mail.com"
