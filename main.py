from js import document
from pyodide.ffi import create_proxy
import re

def accountCreation(event=None):
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value
    output = document.getElementById("output")

    if len(username) < 7:
        output.innerText = "Username must be at least 7 characters long."
        return

    if len(password) < 10:
        output.innerText = "Password must be at least 10 characters long."
        return

    if not re.search("[a-zA-Z]", password):
        output.innerText = "Password must contain at least one letter."
        return

    if not re.search("[0-9]", password):
        output.innerText = "Password must contain at least one number."
        return

    output.innerText = "Account successfully created."


def teamChecker(event=None):
    reg = document.querySelector('input[name="registration"]:checked')
    clear = document.querySelector('input[name="clearance"]:checked')
    section = document.getElementById("section").value
    output = document.getElementById("teamOutput")

    if not reg or not clear:
        output.innerText = "Please answer all questions first."
        return

    if reg.value != "registered":
        output.innerText = "Not eligible. Please complete registration."
        return

    if clear.value != "cleared":
        output.innerText = "Medical clearance required."
        return

    output.innerText = f"Congratulations! You are part of the {section.upper()} team."


def loadPlayers(event=None):
    players = [
        "ACLARO, JOHN TRISTAN E.",
        "AGUILAR, ARIANNE S.",
        "AMANTE, RAILEY L.",
        "BANZALI, DYLAN EURI M.",
        "BULO, EADEN RIEV A."
    ]

    list_element = document.getElementById("playerList")

    for player in players:
        li = document.createElement("li")
        li.innerText = player
        list_element.appendChild(li)


document.getElementById("createBtn").onclick = create_proxy(accountCreation)
document.getElementById("teamBtn").onclick = create_proxy(teamChecker)
document.getElementById("loadBtn").onclick = create_proxy(loadPlayers)

</py-script>

</body>
</html>