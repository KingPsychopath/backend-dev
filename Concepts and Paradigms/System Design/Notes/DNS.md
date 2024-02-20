
# DNS

The "domain name" or "hostname" is part of a URL. We'll get to the other parts of a URL later.

For example, the URL `https://example.com/path` has a hostname of `example.com`. The `https://` and `/path` portions aren't part of the `domain name -> IP address` mapping that we've been learning about.

## Using the URL API in JavaScript

The `URL` API is built into JavaScript. You can create a [new URL object](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL):

```js
const urlObj = new URL('https://example.com/example-path')
```

And then you can [extract just the hostname](https://developer.mozilla.org/en-US/docs/Web/API/URL):

```js
const urlObj.hostname
console.log(url.hostname); // "example.com"
console.log(url.pathname); // "/example-path"
```

```js
const url = new URL("../cats", "http://www.example.com/dogs");
console.log(url.hostname); // "www.example.com"
console.log(url.pathname); // "/cats"
```

The `URL` constructor in JavaScript takes two arguments: `url` and `base`. If the `url` is a relative URL, like `../cats` in your example, it will be resolved relative to the `base` URL.

In your example, `http://www.example.com/dogs` is the base URL and `../cats` is the relative URL. The `..` in `../cats` means "go up one directory", so it goes up from `/dogs` to the root directory `/`, and then goes into `/cats`. That's why `url.pathname` is `/cats` and not `/dogs`.
Here's a step-by-step breakdown:

1. Start at the base URL: `http://www.example.com/dogs`
2. The `..` in `../cats` means "go up one directory", so go up from `/dogs` to `/`: `http://www.example.com/`
3. Then go into `/cats`: `http://www.example.com/cats`

So, the final URL is `http://www.example.com/cats`, and `url.pathname` is `/cats`.
## Assignment

Complete the `getDomainNameFromURL` function. Given a full URL, it should return the domain (or host) name.

```js
function getDomainNameFromURL(url) {
  // ?
  const urlObj = new URL(url)
  return urlObj.hostname
}

// don't touch below this line

const bootdevURL = 'https://boot.dev/learn/learn-python'
const domainName = getDomainNameFromURL(bootdevURL)
console.log(`The domain name for ${bootdevURL} is ${domainName}`)
```

# What is the Domain Name System?

So we've talked about domain names and what their purpose is, but we haven't talked about the system that's used to do that conversion.

![](assets/f6b8d2e03d899d69c69320caf0059a7d.png)

[DNS](https://en.wikipedia.org/wiki/Domain_Name_System), or the "Domain Name System", is the phonebook of the internet. Humans connect to websites through [domain names](https://en.wikipedia.org/wiki/Domain_name), like [Boot.dev](https://boot.dev). DNS "resolves" these domain names to find the associated [IP addresses](https://en.wikipedia.org/wiki/Internet_Protocol) so that web clients can load the resources for the specific address.

> [!NOTE]
> In the context of DNS, "resolves" means it translates, or converts, the human-readable domain names like "example.com" into IP addresses like 192.0.2.1 that computers use to locate each other on the internet.
>
>  It's like a lookup operation in a dictionary or a phonebook, translating words (or names) into an associated piece of data (like a definition or a phone number).

## How does DNS Work?

We'll go into more detail on DNS in a future course, but to give you a simplified idea of how it works, let's introduce ICANN (Internet Corporation for Assigned Names & Numbers) . [ICANN](https://www.icann.org/) is a not-for-profit organization that manages DNS for the entire internet.

Whenever your computer attempts to resolve a domain name, it contacts your ISP (Internet Service Provider) to start the request and then it contacts one of ICANN's ["root nameservers"](https://en.wikipedia.org/wiki/Root_name_server) whose address is included in your computer's networking configuration. From there, that nameserver can gather the domain records for a specific domain name from their distributed DNS databases.

If you think of DNS as a phonebook, ICANN is the publisher that keeps the phonebook in print and available.

ICANN doesn't actually sell the domains though, they're a non-profit; there are accredited registrars re-selling the domains. (on behalf of ICANN essentially)

## DNS Records

There are many distributed DNS databases, and they basically store DNS records which are key:value pairs matching domains to IP addresses or other domains/hostnames.

There are many types of DNS Records, one is called an **A Record -> IP**. The A Record points to a certain IP address and returns this to the client.

**CNAME -> Domain** points to another domain and returns this to the client, who then uses that domain to find an A Record that points to valid IP Address.

Clients can cache IP Addresses (You can flush them with `ipconfig /flushdns` ), and store them to disk meaning we don't have to do the whole DNS process for an IP address to a domain we have already connected to before.

# Subdomains

We learned about how a domain name resolves to an IP address, which is just a computer on a network - often the internet.

A _subdomain_ prefixes a domain name, allowing a domain to route network traffic to many different servers and resources.

For example, the [Boot.dev](https://boot.dev) website that you're on right now is hosted on a different computer than our blog. Our blog, found at [blog.boot.dev](https://blog.boot.dev) is hosted on our "blog" subdomain.

# Domains vs Hostnames

A domain is a group of hostnames. So, example.com is a domain -- but ftp.example.com is a hostname.

A hostname will resolve to one or more IP addresses, and the domain will be a grouping of them with a common suffix. Also note that example.com can also be a hostname, and it still part of the example.com domain.
### Analogy

Let's  take as an example John Smith, his name is composed of 2 parts:
*Smith that refer to the whole family* [[Domain]]
*John that refer to him specifically* [[Hostname]]

You use the hostname to refer to a machine that "host" services.
You use the domain to refer to a logical network of machines.

**Out of URLs like [www.google.com](http://www.google.com), what part is the hostname and what part is the domain?**

The www is the host, the google.com is the domain.
The com. is the top level domain(tld) family. So every IP until that belongs to it.
