// // src/Componentsold/404Page.js

// import React from 'react';
// import './404page.css';
// const NotFoundPage = () => {
//     return (
//         // <div>
//         //     <h1>404 - Page Not Found</h1>
//         //     <p>Sorry, the page you are looking for does not exist.</p>
//         // </div>

// {/* <section class="py-3 py-md-5 min-vh-100 d-flex justify-content-center align-items-center">
//   <div class="container">
//     <div class="row">
//       <div class="col-12">
//         <div class="text-center">
//           <h2 class="d-flex justify-content-center align-items-center gap-2 mb-4">
//             <span class="display-1 fw-bold">4</span>
//             <i class="bi bi-exclamation-circle-fill text-danger display-4"></i>
//             <span class="display-1 fw-bold bsb-flip-h">4.</span>
//           </h2>
//           <h3 class="h2 mb-2">Oops! You're lost.</h3>
//           <p class="mb-5">The page you are looking for was not found.</p>
//           <a class="btn bsb-btn-5xl btn-dark rounded-pill px-5 fs-6 m-0" href="#!" role="button">Back to Home</a>
//         </div>
//       </div>
//     </div>
//   </div>
// </section> */}


//     );
// };

// export default NotFoundPage;


// import React from 'react';
// import './404page.css';
// const NotFoundPage = () => {
//     return (
//         <div>
//             <h1>404 - Page Not Found</h1>
//             <p>Sorry, the page you are looking for does not exist.</p>
//         </div>

//     );
// };

// export default NotFoundPage;




import React from 'react';
import './404page.css'; // Assuming you have a CSS file named NotFoundPage.css for styling

const NotFoundPage = () => {
    return (
    

        <div class="section">
            <h1 class="error">404</h1>
            <div class="page">Ooops!!! The page you are looking for is not found</div>
            <a class="back-home" href="/">Back to home</a>
      </div>

       
    );
}

export default NotFoundPage;

