# AsyncRequestQueue

`AsyncRequestQueue` is a simple JavaScript class that manages a queue of asynchronous tasks. It ensures that no more than a specified number of tasks are running concurrently.

## Task

Create an AsyncRequestQueue class that manages a queue of asynchronous tasks. It returns a promise that resolves when all tasks have finished.

## Usage

First, create a new `AsyncRequestQueue`:

```javascript
const queue = new AsyncRequestQueue();
```

    By default, AsyncRequestQueue allows up to 3 tasks to run concurrently. You can specify a different limit when you create the queue:

    You can also specify the maximum number of tasks that can run concurrently:

    ```javascript
    const queue = new AsyncRequestQueue({ maxConcurrent: 5 });
    ```

    To add a task to the queue, call the add method with a function that returns a promise:

    ```javascript
    queue.add(async () => {
      await doSomething();
    });
    queue.add(async () => {
      await doSomethingElse();
    });

    ```

    The AsyncRequestQueue will automatically start tasks as soon as there is capacity. When a task finishes, it will start the next task in the queue.

    If you want to know when a task has finished, you can pass a callback to the add method:

    ```javascript
    queue.add(async () => {
      await doSomething();
    }, () => {
      console.log('Task finished');
    });
    ```
    If you want to know when all tasks have finished, you can use the `onEmpty` method:

    ```javascript
    queue.onEmpty(() => {
      console.log('All tasks finished');
    });
    ```
    If you want to cancel all pending tasks, you can use the `clear` method:

    ```javascript
    queue.clear();
    ```

## Methods

add(promiseFactory)
Adds a task to the queue. The task is represented by a function (promiseFactory) that returns a promise. The task will start as soon as there are less than maxConcurrent tasks running.

run()
Starts the next task in the queue if there are less than maxConcurrent tasks running. This method is called automatically when a task is added to the queue or a task finishes, so you usually don't need to call it yourself.

    ## License
