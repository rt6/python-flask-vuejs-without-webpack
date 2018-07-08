<template>
  <div>
    <div class="columns" style="background-color:#dfe6e9">
      <div class="column is-2">
          <div class="container box" style="width:200px; background-color:#fff">
            <aside class="menu">
              <p class="menu-label">
                General
              </p>
              <ul class="menu-list">
                <li><a>Dashboard</a></li>
                <li><a>Customers</a></li>
              </ul>
              <p class="menu-label">
                Administration
              </p>
              <ul class="menu-list">
                <li><a>Team Settings</a></li>
                <li>
                  <a class="is-active">Manage Your Team</a>
                  <ul>
                    <li><a>Members</a></li>
                    <li><a>Plugins</a></li>
                    <li><a>Add a member</a></li>
                  </ul>
                </li>
                <li><a>Invitations</a></li>
                <li><a>Cloud Storage Environment Settings</a></li>
                <li><a>Authentication</a></li>
              </ul>
              <p class="menu-label">
                Transactions
              </p>
              <ul class="menu-list">
                <li><a>Payments</a></li>
                <li><a>Transfers</a></li>
                <li><a>Balance</a></li>
              </ul>
            </aside>    
          </div>
      </div>

      <div class="column is-6">
        <section class="section">
          <div class="container">
            <nav class="level box">
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Tweets</p>
                  <p class="title">3,456</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Following</p>
                  <p class="title">123</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Followers</p>
                  <p class="title">456K</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Likes</p>
                  <p class="title">789</p>
                </div>
              </div>
            </nav>
        
            <div class="columns">
              <div class="column">
                <div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                    </figure>
                  </div>
                  <div class="card-content">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-48x48">
                          <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                        </figure>
                      </div>
                      <div class="media-content">
                        <p class="title is-4">John Smith</p>
                        <p class="subtitle is-6">@johnsmith</p>
                      </div>
                    </div>
                    <div class="content">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                      Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                      <a href="#">#css</a> <a href="#">#responsive</a>
                      <br>
                      <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                    </div>
                  </div>
                </div>
              </div>
              <div class="column">
                <div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                    </figure>
                  </div>
                  <div class="card-content">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-48x48">
                          <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                        </figure>
                      </div>
                      <div class="media-content">
                        <p class="title is-4">John Smith</p>
                        <p class="subtitle is-6">@johnsmith</p>
                      </div>
                    </div>
                    <div class="content">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                      Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                      <a href="#">#css</a> <a href="#">#responsive</a>
                      <br>
                      <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        
            <table class="table is-bordered">
              <thead>
                <tr>
                  <th><abbr title="Position">Pos</abbr></th>
                  <th>Team</th>
                  <th><abbr title="Played">Pld</abbr></th>
                  <th><abbr title="Won">W</abbr></th>
                  <th><abbr title="Drawn">D</abbr></th>
                  <th><abbr title="Lost">L</abbr></th>
                  <th><abbr title="Goals for">GF</abbr></th>
                  <th><abbr title="Goals against">GA</abbr></th>
                  <th><abbr title="Goal difference">GD</abbr></th>
                  <th><abbr title="Points">Pts</abbr></th>
                  <th>Qualification or relegation</th>
                </tr>
              </thead>
              <tfoot>
                <tr>
                  <th><abbr title="Position">Pos</abbr></th>
                  <th>Team</th>
                  <th><abbr title="Played">Pld</abbr></th>
                  <th><abbr title="Won">W</abbr></th>
                  <th><abbr title="Drawn">D</abbr></th>
                  <th><abbr title="Lost">L</abbr></th>
                  <th><abbr title="Goals for">GF</abbr></th>
                  <th><abbr title="Goals against">GA</abbr></th>
                  <th><abbr title="Goal difference">GD</abbr></th>
                  <th><abbr title="Points">Pts</abbr></th>
                  <th>Qualification or relegation</th>
                </tr>
              </tfoot>
              <tbody>
                <tr>
                  <th>1</th>
                  <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C." title="Leicester City F.C.">Leicester City</a> <strong>(C)</strong>
                  </td>
                  <td>38</td>
                  <td>23</td>
                  <td>12</td>
                  <td>3</td>
                  <td>68</td>
                  <td>36</td>
                  <td>+32</td>
                  <td>81</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
                </tr>
                <tr>
                  <th>2</th>
                  <td><a href="https://en.wikipedia.org/wiki/Arsenal_F.C." title="Arsenal F.C.">Arsenal</a></td>
                  <td>38</td>
                  <td>20</td>
                  <td>11</td>
                  <td>7</td>
                  <td>65</td>
                  <td>36</td>
                  <td>+29</td>
                  <td>71</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
                </tr>
                <tr>
                  <th>3</th>
                  <td><a href="https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C." title="Tottenham Hotspur F.C.">Tottenham Hotspur</a></td>
                  <td>38</td>
                  <td>19</td>
                  <td>13</td>
                  <td>6</td>
                  <td>69</td>
                  <td>35</td>
                  <td>+34</td>
                  <td>70</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
                </tr>
                <tr class="is-selected">
                  <th>4</th>
                  <td><a href="https://en.wikipedia.org/wiki/Manchester_City_F.C." title="Manchester City F.C.">Manchester City</a></td>
                  <td>38</td>
                  <td>19</td>
                  <td>9</td>
                  <td>10</td>
                  <td>71</td>
                  <td>41</td>
                  <td>+30</td>
                  <td>66</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Play-off_round" title="2016–17 UEFA Champions League">Champions League play-off round</a></td>
                </tr>
                <tr>
                  <th>5</th>
                  <td><a href="https://en.wikipedia.org/wiki/Manchester_United_F.C." title="Manchester United F.C.">Manchester United</a></td>
                  <td>38</td>
                  <td>19</td>
                  <td>9</td>
                  <td>10</td>
                  <td>49</td>
                  <td>35</td>
                  <td>+14</td>
                  <td>66</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Group_stage" title="2016–17 UEFA Europa League">Europa League group stage</a></td>
                </tr>
                <tr>
                  <th>6</th>
                  <td><a href="https://en.wikipedia.org/wiki/Southampton_F.C." title="Southampton F.C.">Southampton</a></td>
                  <td>38</td>
                  <td>18</td>
                  <td>9</td>
                  <td>11</td>
                  <td>59</td>
                  <td>41</td>
                  <td>+18</td>
                  <td>63</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Group_stage" title="2016–17 UEFA Europa League">Europa League group stage</a></td>
                </tr>
                <tr>
                  <th>7</th>
                  <td><a href="https://en.wikipedia.org/wiki/West_Ham_United_F.C." title="West Ham United F.C.">West Ham United</a></td>
                  <td>38</td>
                  <td>16</td>
                  <td>14</td>
                  <td>8</td>
                  <td>65</td>
                  <td>51</td>
                  <td>+14</td>
                  <td>62</td>
                  <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Third_qualifying_round" title="2016–17 UEFA Europa League">Europa League third qualifying round</a></td>
                </tr>
                <tr>
                  <th>8</th>
                  <td><a href="https://en.wikipedia.org/wiki/Liverpool_F.C." title="Liverpool F.C.">Liverpool</a></td>
                  <td>38</td>
                  <td>16</td>
                  <td>12</td>
                  <td>10</td>
                  <td>63</td>
                  <td>50</td>
                  <td>+13</td>
                  <td>60</td>
                  <td></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Body',
  data: function () {
    return {
    }
  },
  components: {
  },
  methods:{
 },
}
</script>

<style>
</style>
