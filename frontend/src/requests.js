import axios from "axios";

export const auth_get = (url) => {
  return new Promise((resolve, reject) =>{
  var access_token = localStorage.getItem("access_token");
  const refresh_token = localStorage.getItem("refresh_token");
  var resp_data;
  const data = axios.get("http://127.0.0.1:8080" + url, {
    headers: { authorization: `${access_token}` },
  });
  data.then((response) => {
    resp_data = response.data;
    resolve(resp_data);
  });
  data.catch((err) => {
    const values = {
      refresh_token: refresh_token,
    };
    axios
      .post("http://127.0.0.1:8080" + "/api/auth/refresh", values)
      .then((response) => {
        err.value = response.data.error;
        if (err.value) {
          reject(err.value);
        } else {
          access_token = response.data.access_token;
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          const data = axios.get("http://127.0.0.1:8080" + url, {
            headers: { authorization: `${access_token}` },
          });
          data.then((response) => {
            resp_data = response.data;
            console.log(resp_data);
            resolve(resp_data);
          });
        }
      });
  });
})
};

export const auth_post = (url, values) => {
  return new Promise((resolve, reject) =>{
  var access_token = localStorage.getItem("access_token");
  const refresh_token = localStorage.getItem("refresh_token");
  var resp_data;
  const data = axios.post("http://127.0.0.1:8080" + url, values, {
    headers: { authorization: `${access_token}` },
  });
  data.then((response) => {
    resp_data = response.data;
    resolve(resp_data)
  });
  data.catch((err) => {
    const values = {
      refresh_token: refresh_token,
    };
    axios
      .post("http://127.0.0.1:8080" + "/api/auth/refresh", values)
      .then((response) => {
        err.value = response.data.error;
        if (err.value) {
          reject(err.value)
        } else {
          access_token = response.data.access_token;
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          const data = axios.post("http://127.0.0.1:8080" + url, values, {
            headers: { authorization: `${access_token}` },
          });
          data.then((response) => {
            resp_data = response.data;
            console.log(resp_data);
            resolve(resp_data)
          });
        }
      });
  });
})
};
