const paths = {
  root: '/api',
  items: '/api/items',
  getItemUrl(id) {
    return `/api/items/${id}`;
  },
};

const messageTypes = {
  warning: 'warning',
  primary: 'primary',
  danger: 'danger',
  success: 'success',
};

export { paths, messageTypes };
