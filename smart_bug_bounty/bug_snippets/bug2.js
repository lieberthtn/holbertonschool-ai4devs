/**
 * BUG BOUNTY CASE #2
 * Language: JavaScript
 * Intended: Fetch a status update asynchronously.
 * Current issue: Missing promise handling/await logic.
 */

async function checkServerStatus() {
    let currentStatus = "offline";

    // Simulating an async network call
    // The developer forgot that setTimeout doesn't block execution
    setTimeout(() => {
        currentStatus = "online";
        console.log("Status changed to online internally.");
    }, 200);

    return currentStatus;
}

// Execution flow
checkServerStatus().then(val => {
    console.log("Server is currently: " + val);
});
