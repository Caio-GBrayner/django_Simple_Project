document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.access) {
            document.getElementById('loginResult').textContent = 'Login successful!';
            localStorage.setItem('token', data.access);
        } else if (data.detail) {
            document.getElementById('loginResult').textContent = 'Login failed: ' + data.detail;
        } else {
            document.getElementById('loginResult').textContent = 'Login failed: Unknown error.';
        }
    })
    .catch(error => {
        document.getElementById('loginResult').textContent = 'Login failed: ' + error;
    });
});

async function fetchProtectedData() {
    const token = localStorage.getItem('token');
    if (!token) {
        console.error('No token found, please login first.');
        return;
    }

    const response = await fetch('/api/some-protected-endpoint/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const data = await response.json();
        console.log('Protected data:', data);
    } else {
        console.error('Failed to fetch protected data:', await response.json());
    }
}
