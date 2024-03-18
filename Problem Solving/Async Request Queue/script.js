class AsyncRequestQueue {
    constructor(maxConcurrent = 3) {
      this.maxConcurrent = maxConcurrent;
      this.running = 0;
      this.queue = [];
    }

    // Add a task to the queue
    add(promiseFactory) {
      this.queue.push(promiseFactory);
      this.run();
    }

    // Run the next task if we're not at max capacity
    run() {
      if (this.running >= this.maxConcurrent || this.queue.length === 0) {
        return;
      }

      this.running++;
      const promiseFactory = this.queue.shift(); // Get the next task from the queue
      promiseFactory()
        .then(() => { // When the task is done, run the next task
          this.running--;
          this.run();
        })
        .catch(() => { // If a task fails, we don't want to stop the queue from running
          this.running--;
          this.run();
        });
    }
  }

//  Usage

const queue = new AsyncRequestQueue();

// Add tasks to the queue
for (let i = 0; i < 10; i++) {
  queue.add(() => new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Finished task ${i}`);
      resolve();
    }, 1000 * (i % 3)); // Each task takes 1-3 seconds
  }));
}
