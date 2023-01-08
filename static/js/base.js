"use strict";

$("#delete-user").click(() => {
    if(confirm("Delete user?")) {
        $("#delete-user-form").submit();
    }
});