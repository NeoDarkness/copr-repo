%define debug_package %{nil}
%global __strip /bin/true
%define __brp_check_rpaths %{nil}

Name:           postman
Version:        12.16.3
Release:        %autorelease
Summary:        Postman API Platform

License:        Proprietary
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils

AutoReqProv:    no

Requires:       hicolor-icon-theme

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -n Postman

%build
# Nothing to build

%install
install -d %{buildroot}/opt/postman
cp -a . %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -sf ../../opt/postman/Postman \
    %{buildroot}%{_bindir}/postman

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/postman.desktop

install -Dm644 \
    app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/pixmaps/postman.png

%check
# No test suite available

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/pixmaps/postman.png

%changelog
%autochangelog