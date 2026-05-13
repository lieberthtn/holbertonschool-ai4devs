/**
 * Bug Bounty Challenge - Case 2
 * Intended to demonstrate a common asynchronous mistake
 * in JavaScript where a value is returned before it is updated.
 */

async function fetchData() {
    let status = "pending";
    
    // Simulating an asynchronous operation
    // The developer forgot that setTimeout does not return a promise
    // and they are not 'awaiting' the change.
    setTimeout(() => {
        status = "completed";
        console.log("Status updated inside timeout");
    }, 500);

    return status;
}

// Execution
fetchData().then(res => {
    console.log("Final Result: " + res); // Expected "completed", gets "pending"
});
