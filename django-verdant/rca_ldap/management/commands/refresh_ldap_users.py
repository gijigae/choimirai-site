from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from django_auth_ldap.backend import LDAPBackend


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # Get LDAP backend
        ldap = LDAPBackend()

        for user in User.objects.all():
            # Check if user is an LDAP user
            if not user.has_usable_password():
                # Populate user details
                print "Refreshing '" + user.username + "' ",
                if ldap.populate_user(user.username):
                    print "Success!"
                    # User found and populated

                    # Make sure this account is activated
                    user.is_active = True
                    user.save()
                else:
                    print "Not found"
                    # User account not found in LDAP
                    # This means that the user either no longer exists
                    # or no longer has privilages to access the CMS
                    # We must deactivate their account to prevent them
                    # from recieving notification emails

                    # Make sure this account is deactivated
                    user.is_active = False
                    user.save()