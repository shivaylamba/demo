class Roles:
    def __init__(self):
        self._roles = ['role1', 'role2', 'role3']
        self._roles_resource_access = {'role1': [
            {'resource': 'R3', 'action': 'delete'}, {'resource': 'R4', 'action': 'write'}],
            'role2': [{'resource': 'R1', 'action': 'write'}, {'resource': 'R2', 'action': 'read'}]}

    def get_roles(self):
        return self._roles_resource_access
