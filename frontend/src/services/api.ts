import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const loginUser = (data: any) =>
  API.post("/auth/login", data);

export const getTasks = () =>
  API.get("/tasks/");
