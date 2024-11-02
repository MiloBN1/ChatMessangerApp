import axios from 'axios';

// Create an Axios instance
const apiClient = axios.create({
  baseURL: 'http://localhost:8000',  // Base URL for your Django backend
  withCredentials: true,             // This allows cross-origin requests to send cookies
});

// Add a request interceptor to include the CSRF token
apiClient.interceptors.request.use((config) => {
  const csrfToken = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
    ?.split('=')[1];
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken;  // Add CSRF token to headers
  }
  return config;
});

export default apiClient;
