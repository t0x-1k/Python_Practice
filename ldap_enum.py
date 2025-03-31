from ldap3 import Server, Connection, ALL, SUBTREE
import argparse

def enumerate_ldap_users(ldap_server: str, base_dn: str, username: str = None, password: str = None):
    """
    Enumerates usernames from an LDAP v2 server.

    Usages: python ldap_enum.py ldap://192.168.1.1 "DC=example,DC=com"

    Args:
        ldap_server (str): LDAP server address (e.g., ldap://192.168.1.1).
        base_dn (str): Base distinguished name to search from.
        username (str, optional): Username for authentication. Defaults to None (anonymous bind).
        password (str, optional): Password for authentication. Defaults to None.
    """
    try:
        # Initialize the LDAP server (LDAP v2)
        server = Server(ldap_server, get_info=ALL)

        # Establish connection (anonymous bind or authenticated)
        conn = Connection(server, user=username, password=password, auto_bind=True)

        # Search filter for retrieving all users (modify if necessary)
        search_filter = "(objectClass=person)"

        print(f"🔍 Searching for users in {base_dn}...")
        
        # Perform LDAP search
        conn.search(search_base=base_dn,
                    search_filter=search_filter,
                    search_scope=SUBTREE,
                    attributes=['cn', 'uid', 'sAMAccountName', 'displayName'])

        if not conn.entries:
            print("❌ No users found!")
            return

        # Print found usernames
        print("\n📝 Enumerated Users:\n" + "=" * 40)
        for entry in conn.entries:
            cn = entry.cn.value if hasattr(entry, 'cn') else "N/A"
            uid = entry.uid.value if hasattr(entry, 'uid') else "N/A"
            sam = entry.sAMAccountName.value if hasattr(entry, 'sAMAccountName') else "N/A"
            display = entry.displayName.value if hasattr(entry, 'displayName') else "N/A"

            print(f"Common Name (CN): {cn}")
            print(f"User ID (UID): {uid}")
            print(f"sAMAccountName: {sam}")
            print(f"Display Name: {display}")
            print("-" * 40)

        # Unbind after completion
        conn.unbind()

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LDAP v2 Username Enumeration Script")
    parser.add_argument("ldap_server", help="LDAP server (e.g., ldap://192.168.1.1)")
    parser.add_argument("base_dn", help="Base DN (e.g., DC=example,DC=com)")
    parser.add_argument("--username", help="LDAP bind username (optional)", default=None)
    parser.add_argument("--password", help="LDAP bind password (optional)", default=None)

    args = parser.parse_args()

    enumerate_ldap_users(args.ldap_server, args.base_dn, args.username, args.password)
