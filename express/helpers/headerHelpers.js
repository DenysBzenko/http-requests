function setHeader(res, headerName, headerValue) {
  if (typeof headerName === 'string' && headerName !== '' && typeof headerValue === 'string') {
    res.setHeader(headerName, headerValue);
  } 
}

  

  function getHeader(req, headerName) {
    const headerValue = req.headers[headerName.toLowerCase()];
    return headerValue || 'Header not found';
  }
  
  module.exports = { setHeader, getHeader };
  