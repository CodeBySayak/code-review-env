class EasyTask:
    def get_problem(self):
        return {
            "title": "Hardcoded password",
            "code": "password = '12345'",
            "goal": "Find security issue"
        }

    def evaluate(self, action):
        if action == "flag_security":
            return 1.0, True, {"msg": "Hardcoded secret"}
        return 0.0, True, {}


class MediumTask:
    def get_problem(self):
        return {
            "title": "SQL Injection",
            "code": "query = 'SELECT * FROM users WHERE id=' + user_input",
            "goal": "Find vulnerability"
        }

    def evaluate(self, action):
        if action == "flag_security":
            return 1.0, True, {"msg": "SQL Injection"}
        return 0.0, True, {}


class HardTask:
    def get_problem(self):
        return {
            "title": "Remote Code Execution",
            "code": "eval(user_input)",
            "goal": "Find critical issue"
        }

    def evaluate(self, action):
        if action == "flag_security":
            return 1.0, True, {"msg": "RCE risk"}
        elif action == "approve":
            return -1.0, True, {"msg": "Dangerous approval"}
        return 0.0, True, {}