const paths = {
  root: '/',
  items: '/items',
  getItemUrl(id) {
    return `/items/${id}`;
  },
};

const messageTypes = {
  warning: 'warning',
  primary: 'primary',
  danger: 'danger',
  success: 'success',
};

export { paths, messageTypes };
