<!--
 * @Author: sunyudi
 * @Date: 2020-06-06 11:37:13
 * @LastEditTime: 2020-10-17 15:18:04
--> 
# Tell you some notes about Vue

## CSS Lint of .vue in VSCode

1. Open a `.vue` file in VSCode

2. Click the `Vue` button on right-bottom corner

    ![](../assets/2020-06-06-17-00-37.png)

3. Select the marked option

    ![](../assets/2020-06-06-17-02-41.png)

4. Choose `HTML`

    ![](../assets/2020-06-06-17-03-47.png)

5. Done!

## Vue Directive

1. v-bind

    <template>
        <img v-bind:src="imageSrc">
    </template>

    <script>
        export default {
            name: "test",
            data(){
                imageSrc: "xxxxxxxxxx"
            },
        }
    </script>

2. v-if

    <template>
        <span v-if="seen"> Now you can see me </span>
    </template>

    <script>
        export default {
            name: "test",
            data(){
                seen: true
            },
        }
    </script>

3. v-for

    <template>
        <li v-for="todo in todos">
            {{ todo.text }}
        </li>
    </template>

    <script>
        export default {
            name: "test",
            data(){
                todos: [
                    {"text": "aaa"},
                    {"text": "bbb"}
                ]
            },
        }
    </script>

4. v-on

    <template>
        <p>{{ message }}</p>
        <button v-on:click="reverseMessage">Reverse Message</button>
    </template>

    <script>
        export default {
            name: "test",
            data(){
                message: "Hello Vue.js!"
            },
            methods: {
                reverseMessage: function () {
                    this.message = this.message.split('').reverse().join('')
                }
            }
        }
    </script>

5. v-model (two-way binding)

    <template>
        <p>{{ message }}</p>
        <input v-model="message">
    </template>

    <script>
        export default {
            name: "test",
            data(){
                message: "Hello Vue.js!"
            }
        }
    </script>


## Cross-site Problem

When making a http request in vue, you may meet cross-site problem. So the connection will be blocked by CORS policy.

    this.$http.get('/api/sample')
        .then(response => {

        })
        .catch(error => {

        });

The reason is "The front end and back end are in different networks, although you start them on one computer."

To solve this problem, just create "vue.config.js" file and add the following code

    module.exports = {
        devServer: {
            proxy: 'http://127.0.0.1:5000'  // your back_end server
        },
    }