import os
import nomad




host_name = os.environ.get("NOMAD_HOST", "localhost:4646")
nomad_url = f"https://{host_name:4646}"

def connect_try(url):
    user = os.getlogin()
    n = nomad.Nomad(url, secure=True, verify=True, cert=f"/Users/{user}/.gemini/ca_certs.pem")
    jobs = n.jobs.get_jobs()
    for job in jobs:
        print(job['Name'])


if __name__ == "__main__":
    connect_try(nomad_url)
