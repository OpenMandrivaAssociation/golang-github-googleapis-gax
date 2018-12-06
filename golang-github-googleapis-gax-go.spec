# Run tests in check section
%bcond_without check

%global goipath         github.com/googleapis/gax-go
Version:                2.0.0

%global common_description %{expand:
Google API Extensions for Go (gax-go) is a set of modules which aids the 
development of APIs for clients and servers based on gRPC and Google API 
conventions.

Application code will rarely need to use this library directly, but the 
code generated automatically from API definition files can use it to simplify 
code generation and to provide more convenient and idiomatic API surface.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Google API Extensions for Go 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/status)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018  Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- First package for Fedora

